import psycopg2

def deleteTop3Rows():
    connection_string = "postgres://vlogs_5aku_user:RhzYf0iDaOgMZhhVG9T8M0MZLMZyXfnM@dpg-ck5gosei9prc73bkkc1g-a.oregon-postgres.render.com/vlogs_5aku"

    try:
        # Establish a connection using the connection string
        connection = psycopg2.connect(connection_string)

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Define the DELETE query to delete the top 3 rows based on a condition
        delete_query = """
        DELETE FROM blogtable
        WHERE blogid IN (
            SELECT blogid
            FROM blogtable
            ORDER BY blogid
            LIMIT 3
        );
        """

        # Execute the DELETE query
        cursor.execute(delete_query)

        # Commit the changes to the database
        connection.commit()

        print("Top 3 rows deleted successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL or deleting rows:", error)

    finally:
        # Close the cursor and the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

# Call the function to delete the top 3 rows
deleteTop3Rows()
