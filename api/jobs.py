import flask
from flask import jsonify, make_response
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api', __name__
)


@blueprint.route('/api/jobs')
def get_jobs():
    jobs = db_session.create_session().query(Jobs).all()
    return jsonify({"jobs": [j.to_dict(only=["job",
                                             "work_size",
                                             "is_finished",
                                             "team_leader_data.surname",
                                             "team_leader_data.name"])
                             for j in jobs]})


@blueprint.route('/api/jobs/<int:job_id>')
def get_job_by_id(job_id):
    job = db_session.create_session().get(Jobs, job_id)
    if job is not None:
        return jsonify(job.to_dict())
    else:
        return make_response(jsonify(
            {"error": "No such job"}), 404)
