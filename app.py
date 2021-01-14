from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, ObjectType, QueryType, MutationType, snake_case_fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML

from flask import request, jsonify

from api import app, db
from api import author_model, book_model
import api.author_resolver as author_resolver
import api.book_resolver as book_resolver

query = QueryType()
mutation = MutationType()

query.set_field('authors', author_resolver.resolve_authors)
query.set_field('author', author_resolver.resolve_author)

query.set_field('books', book_resolver.resolve_books)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    query,
    mutation,
    # snake_case_fallback_resolvers
)

@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route('/graphql', methods=['POST'])
def graphql_server():
    data =  request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
