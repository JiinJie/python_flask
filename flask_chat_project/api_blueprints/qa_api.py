# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 11:42
# @Author  : jinjie

# question and answer model


from flask import Blueprint, g, request,render_template,redirect,url_for,flash
from decorators import login_required
from .forms import CommitQuest,CommitAnswer
from commons import db
from db_model import CommitQuestModel,AnswerModel

bp_quest = Blueprint("quest",__name__,url_prefix="/")


@bp_quest.route('/index')
def index_page():
    # 按照时间倒叙所有  需将创建时间转为文本再取负（倒叙）
    quest = CommitQuestModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html",questions=quest)


@bp_quest.route('question/public',methods=['GET','POST'])
@login_required
def public_quest_page():
    # 判断用户是否登录，若未登录则跳转至登录页面
    # if hasattr(g,'user'):
    # 缺点：每个视图都需要进行判断。因此可以用装饰器在每个接口访问前进行判断。查看decorators.py详情
    if request.method == 'GET':
        return render_template("public_quest.html")
    if request.method == 'POST':
        form = CommitQuest(request.form)
        if form.validate():
            title = form.quest_title.data
            content = form.quest_content.data
            commit_quest = CommitQuestModel(title=title,content=content,author=g.user)
            db.session.add(commit_quest)
            db.session.commit()
            return redirect(url_for("quest.index_page"))
        else:
            flash("标题或内容格式错误！")
            return redirect(url_for("quest.public_quest_page"))


@bp_quest.route("/question/<int:question_id>")
@login_required
def question_detail_page(question_id):
    question_data = CommitQuestModel.query.get(question_id)
    return render_template("chat_detail_page.html",question=question_data)


@bp_quest.route("/answer",methods=['POST'])
@login_required
def commit_answer():
    form = CommitAnswer(request.form)
    #question_uuid = form.question_uuid.data
    question_id = form.question_id.data
    print(question_id)
    if form.validate():
        content = form.reply_content.data
        # question_id = form.question_id.data
        answer_data = AnswerModel(content=content,quest_id=question_id,reply_author=g.user)  #TODO 为什么有的用映射名，有的要用表名？
        #answer_data = AnswerModel(content=content,bind_quest_id=question_id,reply_author=g.user)
        db.session.add(answer_data)
        db.session.commit()
        flash("提交成功")
        return redirect(url_for("quest.question_detail_page",question_id=question_id))
    else:
        flash("数据验证异常：回复失败！")
        print("提交失败")
        if question_id:
            return redirect(url_for("quest.question_detail_page",question_id=question_id))
        else:
            flash("回复的帖子不存在！")
            return redirect(url_for("quest.index_page"))
