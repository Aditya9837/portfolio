import psycopg2
import os

# Replace with your PostgreSQL connection string
def insertBlog(title,description,imagepath):
    connection_string = "postgres://vlogs_5aku_user:RhzYf0iDaOgMZhhVG9T8M0MZLMZyXfnM@dpg-ck5gosei9prc73bkkc1g-a.oregon-postgres.render.com/vlogs_5aku"

    # Path to the image file you want to upload
    image_file_path = imagepath

    try:
        # Establish a connection using the connection string
        connection = psycopg2.connect(connection_string)

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Read the image file and convert it to bytes
        with open(image_file_path, 'rb') as image_file:
            image_data = image_file.read()

        # Define the INSERT query with placeholders
        insert_query = """
        INSERT INTO blogtable (IMAGE, TITLE, DESCription)
        VALUES (%s, %s, %s)
        """

        # Define the values to be inserted
        values_to_insert = (
            image_data,  # Insert the image data
           title,
            description
        )

        # Execute the INSERT query
        cursor.execute(insert_query, values_to_insert)

        # Commit the changes to the database
        connection.commit()

        print("Image uploaded successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL or uploading the image:", error)

    finally:
        # Close the cursor and the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")
