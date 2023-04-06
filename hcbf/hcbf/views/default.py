from pyramid.view import view_config


@view_config(route_name='journeys_list', renderer='hcbf:templates/journeys-list.jinja2')
def my_view(request):
    page = request.params.get('page', '1')
    page = int(page)
    res = request.db().execute("""
    SELECT * FROM journey LIMIT 50 OFFSET ?""", [page * 50])
    journeys = res.fetchall()
    return {
        'journeys': journeys,
        'previous_page': request.current_route_path(_query={'page': max(0, page - 1)}),
        'current_page_number': page,
        'next_page': request.current_route_path(_query={'page': page + 1 })
    }
