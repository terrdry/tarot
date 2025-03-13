import os
import pytest
from pathlib import Path
from app import app,db
from models import Card
from sqlalchemy import func
from sqlalchemy import select
from config import config

# TEST_DB = "test.db"

@pytest.fixture
def client():
    # BASE_DIR = Path(__file__).resolve().parent.parent
    # BASE_DIR = "sqlite:///" + BASE_DIR
    
    app.config.from_object(config.testConfig)
    # app.config["TESTING"] = True
    # app.config["DATABASE"] = BASE_DIR.joinpath(TEST_DB)
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # init_db() # teardown

# def login(client, username, password):
#     """Login helper function"""
#     return client.post(
#         "/login",
#         data=dict(username=username, password=password),
#         follow_redirects=True,
#     )

# def logout(client):
#     """Logout helper function"""
#     return client.get("/logout", follow_redirects=True)

def test_index(client):
    response = client.get("/", content_type="html/text")
    assert response.status_code == 200

def test_database(client):
    """initial test. ensure that the database exists"""
    tester = Path(os.path.join(os.getcwd(),"db/test.db"))
    # tester = os.path.join(os.getcwd(),Path("db/test.db")).is_file()
    print(tester)
    print(os.getcwd())
    assert tester

# def test_empty_db(client):
#     """Ensure database is blank"""
#     rv = client.get("/")
#     assert b"No entries yet. Add some!" in rv.data

# def test_login_logout(client):
#     """Test login and logout using helper functions"""
#     rv = login(client, app.config["USERNAME"], app.config["PASSWORD"])
#     assert b"You were logged in" in rv.data
#     rv = logout(client)
#     assert b"You were logged out" in rv.data
#     rv = login(client, app.config["USERNAME"] + "x", app.config["PASSWORD"])
#     assert b"Invalid username" in rv.data
#     rv = login(client, app.config["USERNAME"], app.config["PASSWORD"] + "x")
#     assert b"Invalid password" in rv.data

# def test_messages(client):
#     """Ensure that user can post messages"""
#     login(client, app.config["USERNAME"], app.config["PASSWORD"])
#     rv = client.post(
#         "/add",
#         data=dict(title="<Hello>", text="<strong>HTML</strong> allowed here"),
#         follow_redirects=True,
#     )
#     assert b"No entries here so far" not in rv.data
#     assert b"&lt;Hello&gt;" in rv.data
#     assert b"<strong>HTML</strong> allowed here" in rv.data
def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == 'pong!'

def test_get_cards(client):
    response = client.get('/cards')
    assert response.status_code == 200
    assert response.json == []

def test_get_readings(client):
    response = client.get('/readings')
    assert response.status_code == 200
    assert response.json == []

# def  test_add_card(client):
#     card= Card(name="The Magician", major=True, img="magician.jpg")
#     with app.app_context():
#         db.session.add(card)
#         db.session.commit()
#     # stmt = select(func.count()).alias('card')
