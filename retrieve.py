import psycopg2
import os

# Replace 'your_connection_string' with your actual connection string
def retBlogs():
    connection_string = "postgres://vlogs_5aku_user:RhzYf0iDaOgMZhhVG9T8M0MZLMZyXfnM@dpg-ck5gosei9prc73bkkc1g-a.oregon-postgres.render.com/vlogs_5aku"
    try:
        # Establish a connection using the connection string
        connection = psycopg2.connect(connection_string)

        # Create a cursor object using the connection
        cursor = connection.cursor()

        # Define a SELECT query to retrieve image data and other columns from your table
        select_query = """
        SELECT IMAGE, TITLE, DESCription
        FROM blogtable
        """

        # Execute the SELECT query
        cursor.execute(select_query)

        # Fetch all the rows from the result set
        rows = cursor.fetchall()

        # Specify the directory where you want to save the images


        # Create the directory if it doesn't exist
        

        # Iterate through the rows and save the images as files
        blogs=[]
        for row in rows:
            temp={}
            image_data, title, description = row
            
            # Generate a unique file name or use the title as the file name
            file_name = title + ".jpg"  # You may need to adjust the file extension

            # Combine the save directory and file name to create the full file path
            file_path =  'static/imgs/blogs/'+file_name
            temp['imagepath']='/imgs/blogs/'+file_name
            temp['title']=title
            temp['description']=description
            # Save the image data to a file
            with open(file_path, "wb") as file:
                file.write(image_data)
            blogs.append(temp)
        return blogs

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL:", error)

    finally:
        # Close the cursor and the connection
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")
