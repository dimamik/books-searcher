from pathlib import Path

from flask import send_file

from api.server import app
from elastic.get_data_from_elastic import export_to_csv


# TODO Needs to be protected and exposed locally!
@app.route('/get_all_index/<index_name>')
def upload_index(index_name):
    """
    Sends csv drop of database in response to inner server query
    **DANGEROUS!!**
    """
    # TODO Change request to be paginated and so on
    export_to_csv(index_name)
    return send_file(Path('../raw_data/temp.csv'), as_attachment=True, attachment_filename=f'{index_name}_drop.csv')
