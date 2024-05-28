from flask import Blueprint, render_template, request, flash, jsonify, current_app
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/konsultasi')
@login_required
def konsultasi():
    gejala = current_app.sistem_pakar.gejala
    return render_template('konsultasi.html', user=current_user, gejala=gejala)

@views.route('/result', methods=['POST'])
@login_required
def result():
    keluhan = request.form.get('keluhan')
    gejala_list = request.form.getlist('gejala')
    
    penyakit_diduga = current_app.sistem_pakar.aturan_inferensi(keluhan, gejala_list)
    result = ', '.join([current_app.sistem_pakar.penyakit[p] for p in penyakit_diduga]) if penyakit_diduga else 'Tidak ada diagnosis yang cocok. Harap periksa ke dokter untuk diagnosa lebih lanjut.'

    solusi = {current_app.sistem_pakar.penyakit[penyakit]: current_app.sistem_pakar.solusi[penyakit] for penyakit in penyakit_diduga}
    print(f"solusi: {solusi}")  # Debug print
    
    return render_template('result.html', result=result, solusi=solusi, user=current_user)




