from django.shortcuts import render, redirect
import sqlite3

def list_jobs(request):
    con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
    cur = con.cursor()
    cur.execute("select * from jobs")
    jobs = cur.fetchall()
    con.close()
    return render(request,"list_jobs.html", {"jobs" : jobs} )

def add_job(request):
    if request.method == "GET":
        return render(request,'add_job.html')
    else:   # POST
        title = request.POST['title']
        minsal = request.POST['minsal']
        description = request.POST['description']
        con = sqlite3.connect(r"e:\classroom\python\aug16\hr.db")
        cur = con.cursor()
        cur.execute("insert into jobs(title,minsal,description) values (?,?,?)",
                    (title,minsal,description))
        con.commit()
        count = cur.rowcount
        con.close()

        return redirect("/hr/jobs")

