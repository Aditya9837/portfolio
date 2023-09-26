from flask import Flask,render_template,send_file,request
import insert
import retrieve
app=Flask(__name__)
@app.route('/')
def Index():
    blogs=retrieve.retBlogs()
    return render_template('index.html',blogs=blogs)
@app.route('/upload_template')
def upload_template():
    return render_template('uploadblog.html')
@app.route('/upload',methods=['POST'])
def upload():
    title=request.form['title']
    description=request.form['description']
    image=request.files['image']
    image.save('image.jpg')
    insert.insertBlog(title,description,'image.jpg')
    return render_template('uploadblog.html',message='Blog Uploaded')

@app.route('/download')
def download():
    file_path = 'static/resume/Resume (1).pdf'  # Provide the actual path to your file
    filename = 'Aditya_patel_resume.pdf'  # Change the filename as needed

    # Use send_file to send the file to the user's browser
    return send_file(file_path, as_attachment=True, download_name=filename)


if __name__=='__main__':
    app.run(debug=True)