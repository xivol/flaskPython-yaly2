import flask
from flask import jsonify, make_response, request
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


@blueprint.app_errorhandler(404)
def error_not_found(e):
    return make_response(jsonify({"error": e.description}), 404)


@blueprint.route('/api/jobs', methods=['POST'])
def add_jobs():
    if not request.json:
        return make_response(jsonify({"error": "no json"}), 400)

    if not all(key in request.json
               for key in ["job", "work_size", "collaborators",
                           "is_finished", "team_leader"]):
        return make_response(jsonify({"error": "not enough data"}), 400)

    j = Jobs()
    j.job = request.json["job"]
    j.work_size = int(request.json["work_size"])
    j.collaborators = request.json["collaborators"]
    j.is_finished = bool(request.json["is_finished"])
    j.team_leader = int(request.json["team_leader"])
    sess = db_session.create_session()
    sess.add(j)
    sess.commit()
    return make_response(jsonify({"ok": j.id}), 201)


@blueprint.route('/api/jobs', methods=['PUT'])
def change_jobs():
    return flask.abort(500)


@blueprint.route('/api/jobs', methods=['DELETE'])
def delete_jobs():
    return flask.abort(500)
