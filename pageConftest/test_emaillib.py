import pytest
from pageConftest.emaillib import MailAdminClient,Email

@pytest.fixture
def mail_admin():
    return MailAdminClient()

@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)

@pytest.fixture
def receiving_user(mail_admin):
    user = mail_admin.create_user()
    yield user
    mail_admin.delete_user(user)

def test_email_received(sending_user,receiving_user):
    email = Email(subject="hello", body="say hello")
    sending_user.send_mail(email,receiving_user)
    assert email in receiving_user.inbox