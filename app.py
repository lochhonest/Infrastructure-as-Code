db.create_all()

@app.route('/add', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task.content = request.form['content']
        task_content = Todo(content=task.content)

        try:
            db.session.add(content)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
        return render_template('index.html')
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
