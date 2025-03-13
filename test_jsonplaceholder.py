import random
import pytest
from utils.api_client import APIClient

# Base URL for JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client():
    return APIClient(BASE_URL)


def get_random_user(api_client):
    """Get a random user and return their userID and email."""
    response = api_client.get("users")
    assert response.status_code == 200, "Failed to fetch users"

    users = response.json()
    random_user = random.choice(users)
    user_id = random_user["id"]
    email = random_user["email"]

    print(f"Random User ID: {user_id}, Email: {email}")
    return user_id


def get_user_posts(api_client, user_id):
    """Get posts associated with the given userID."""
    response = api_client.get("posts", params={"userId": user_id})
    assert response.status_code == 200, "Failed to fetch posts"

    posts = response.json()
    return posts


def verify_post_ids(posts):
    """Verify that all Post IDs are integers between 1 and 100."""
    for post in posts:
        post_id = post["id"]
        assert isinstance(post_id, int), f"Post ID {post_id} is not an integer"
        assert 1 <= post_id <= 100, f"Post ID {post_id} is out of range"


def create_post(api_client, user_id, title, body):
    """Create a new post for the given userID."""
    new_post = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    response = api_client.post("posts", data=new_post)
    return response


def test_jsonplaceholder_functionality(api_client):
    # Step 1: Get a random user and print their email
    user_id = get_random_user(api_client)

    # Step 2: Get the user's posts and verify Post IDs
    posts = get_user_posts(api_client, user_id)
    verify_post_ids(posts)

    # Step 3: Create a new post and verify the response
    title = "Test Post Title"
    body = "This is the body of the test post."
    response = create_post(api_client, user_id, title, body)

    # Verify the response
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    assert response.json()["id"] == 101, "New post ID should be 101 (mock API behavior)"
    assert response.json()["title"] == title, "Title does not match"
    assert response.json()["body"] == body, "Body does not match"
    assert response.json()["userId"] == user_id, "User ID does not match"

    print("All tests passed successfully!")