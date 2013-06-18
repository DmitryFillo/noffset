# -*- coding: utf-8 -*-

from math import ceil
from sqlalchemy.sql.expression import func

def pagination(db, model, per_page, cursor=False, direction=False, reverse=False):
    """
	No offset fast pagination.

	@param db: SQLAlchemy db object.
	@param model: Model to paginate.

	@param per_page: Per page items.
	@type per_page: number.

	@param cursor: Need page cursor (based on id column). Optional.
	@type cursor: number.

	@param direction: Type of cursor. True means 'next', False means 'prev'. Optional.
	@type direction: boolean.

        @param reverse: If False last item in DB will be first (like newspapers, comments, etc). If True last item in DB will be honestly last.
        @type reverse: boolean.

	@return: dict(data, cursor_next, cursor_prev, pages_total).
    """

    total = db.session.query(func.count(model.id)).first()[0]
    pages = prev = next = None

    if total != 0:
        pages, data = int(ceil(float(total)/float(per_page))), model.query
 
        if cursor:
	    if direction:
                if not reverse:
	            data = data.filter(model.id >= cursor).order_by('id ASC')
                else:
                    data = data.filter(model.id <= cursor).order_by('id ASC')
	    else:
                if not reverse:
	            data = data.filter(model.id <= cursor).order_by('id DESC')
                else:
                    data = data.filter(model.id >= cursor).order_by('id DESC')
	else:
            if not reverse:
	        data = data.order_by('id DESC')
            else:
                data = data.order_by('id ASC')

	data = data.limit(per_page).all()

        if not reverse:
	    if cursor and direction:
	        data.reverse()
        elif cursor and not direction:
                data.reverse()

        if not reverse:
    	    prev, next = data[-1].id-1, data[0].id+1
        else:
            prev, next = data[-1].id+1, data[0].id-1
    else:
        data = False

    return {'data' : data, 'cursor_next' : next, 'cursor_prev' : prev, 'pages_total' : pages}
