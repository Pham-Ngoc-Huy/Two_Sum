import pandas as pd
import logging
import numpy as np

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def combine_find(df, target_sum, column_index, column_sum):
    result = []
    found = [False]

    def backtrack(start, current_sum, current_indices):
        try:
            if found[0]:
                return
            
            if current_sum == target_sum:
                result.append(current_indices[:])
                logging.info(f"Found combination: {current_indices}")
                found[0] = True
                return

            if current_sum > target_sum:
                return   
                 
            for i in range(start, len(df)):
                current_indices.append(df[column_index][i])
                backtrack(i + 1, current_sum + df[column_sum][i], current_indices)
                current_indices.pop()
                if found[0]:
                    break
        except Exception as e:
            logging.error(f"Error occurred: {e}")

    backtrack(0, 0, [])
    return result

def main_combination_result(df, target_sum, column_index, column_sum):
    try:
        # column_index = 'index'
        # column_sum = 'amount'
        combinations = combine_find(df, target_sum, column_index, column_sum)
        df_new = []
        if combinations:
            for combination in combinations:
                logging.info(f"Indices that sum to {target_sum}: {combination}")
                matching_rows = df[df[column_index].isin(combination)]
                df_new.append(matching_rows)
            return pd.concat(df_new).reset_index(drop=True)
        else:
            raise ValueError("No combinations match the target sum.")
    except ValueError as ve:
        logging.info(f"No combinations found that sum to {target_sum}.")
        return pd.DataFrame()

def main():
    data = {
        'index': np.arange(1, 101),
        'amount': np.random.randint(1, 100, size=100)  
    }
    df = pd.DataFrame(data)
    target_sum = 23
    column_index = 'index'
    column_sum = 'amount'
    result_df = main_combination_result(df, target_sum, column_index, column_sum)
    logging.info(f"Done Finding Combination Sum")
    print(result_df)

if __name__ == "__main__":
    main()
