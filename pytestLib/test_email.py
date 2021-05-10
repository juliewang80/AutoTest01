import pytest

from emailtest import Email,MailAdminClient

@pytest.fixture
def mail_admin():
    return MailAdminClient()

@pytest.fixture
def sending_user(mail_admin):
    user = mail_admin.create_user()
    yield user  #之前是setup 之后是teardown
    mail_admin.delete_user(user)

@pytest.fixture
def receiving_user(mail_admin,request):
    # user = mail_admin.create_user()
    # yield user
    # mail_admin.delete_user(user)
    user =mail_admin.create_user()

    def delete_user():
        mail_admin.delete_user(user)

    request.addfinalizer(delete_user)
    return user

def test_email_received(sending_user,receiving_user):
    email = Email(subject="hello", body="say hello")
    sending_user.send_mail(email,receiving_user)
    assert email in receiving_user.inbox