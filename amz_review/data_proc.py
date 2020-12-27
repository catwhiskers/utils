import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_product_by_id(product_id, items_df):
    """
    This takes in an product_id from Personalize so it will be a string,
    converts it to an int, and then does a lookup in a default or specified
    dataframe.

    A really broad try/except clause was added in case anything goes wrong.

    Feel free to add more debugging or filtering here to improve results if
    you hit an error.
    """
    try:
        c_row = items_df[items_df['product_id'] == product_id].iloc[0]
        title = c_row['product_title']
        category = c_row['product_category']

        return [title, category]
    except:
        return "Error obtaining product info"


def compare_personalized_result(original_df, recommendations_response_rerank, items_df):
    ranked_list = []
    item_list = recommendations_response_rerank['personalizedRanking']
    for item in item_list:
        product = get_product_by_id(item['itemId'], items_df)
        ranked_list.append(product)
    ranked_df = pd.DataFrame(ranked_list, columns = ['Original','Re-Ranked'])
    compare_df = pd.concat([original_df, ranked_df], axis=1)
    # pd.set_option('display.max_colwidth', -1)
    # pd.set_option('display.max_rows', None)
    return compare_df


# rerank_user = 49240011
def plot_heat_map(df, figsize=(10,7)):
    df = df.groupby(['product_category']).count()
    df = df.drop(['USER_ID', 'EVENT_VALUE', 'index'], axis=1)
    plt.subplots(figsize=figsize)
    sns.heatmap(df)



def get_user_history(user_id, user_item_df, items_df):
    user_df = user_item_df[user_item_df['USER_ID']==user_id]
    print(user_df)
    all_df = user_df.merge(items_df, left_on='ITEM_ID', right_on='product_id')
    # plot_heat_map(all_df, figsize=(10,5))
    return all_df

