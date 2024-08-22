import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def combine_find(df,sum):
    result = []
    def backtrack(start,current_sum,current_indices,column_index,column_sum):
        try:
            if current_sum == sum:
                result.append(current_indices[:])
                logging.info(f"Found combination: {current_indices}")
                return
            if current_sum > sum:
                return        
            for i in range(start, len(df)):
                current_indices.append(df[column_index][i])
                backtrack(i + 1, current_sum + df[column_sum][i], current_indices,column_index, column_sum)
                current_indices.pop()
        except Exception as e:
            logging.error(f"Error occurred: {e}")
    
    backtrack(0, 0, [])
    return result

def main_combination_result(df,sum):
    try:
        combinations = combine_find(df,sum)
        df_new = []
        # Print results
        if combinations:
            for combination in combinations:
                print(f"Indices that sum to {sum}: {combination}")
                matching_rows = df[df['index'].isin(combination)]
                df_new.append(matching_rows)
                return pd.DataFrame(df_new[1].copy())
        else:
            raise ValueError("No combinations match the target sum.")
    except ValueError as ve:
        logging.info(f"No combinations found that sum to {sum}.")
