# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Title
st.title(":cup_with_straw: Your Smoothie, Your Way! :cup_with_straw:")
st.write("Build your smoothie with your favorite fruits!")

# Input field for name
name_on_order = st.text_input("Name on Smoothie", "")
st.write("The name on your Smoothie will be:", name_on_order)

cnx = st.connection("Snowflake")
session = snx.session()
# Get Snowflake session
session = get_active_session()

# Query fruit options table
my_dataframe = session.table("smoothies.public.fruit_options").select(col("FRUIT_NAME"))

# Multi-select widget directly from dataframe
ingredients_list = st.multiselect(
    "Choose up to 5 ingredients:",
    my_dataframe
    , max_selections=5
)

# If user selected ingredients
if ingredients_list:
    ingredients_string = " ".join(ingredients_list)

    # Submit button
    time_to_insert = st.button('Submit order')

    # if time_to_insert:
    #     # Insert query with both name and ingredients
    #     my_insert_stmt = f"""
    #         INSERT INTO smoothies.public.orders (name_on_order, ingredients)
    #         VALUES ('{name_on_order}', '{ingredients_string.strip()}')
    #     """
    #     st.write("Running query:", my_insert_stmt)  # Debugging ke liye
    #     session.sql(my_insert_stmt).collect()


    if time_to_insert:
        # Insert query with both name and ingredients
        my_insert_stmt = f"""
            INSERT INTO smoothies.public.orders (name_on_order, ingredients)
            VALUES ('{name_on_order}', '{ingredients_string.strip()}')
        """
        session.sql(my_insert_stmt).collect()

        # Success message with customer name
        st.success(f"✅ Your Smoothie is ordered, {name_on_order}! 🍹", icon="🥤")
