from archives.classpages.choserole.choseRole import ChoseRole
from archives.testsPages.adminUserTest.systemManagement.organizationIdentity.organizationIdentity import \
    OrganizationIdentityTest


class AdminUserTest:
    def __init__(self, driver, connection):
        self.driver = driver
        self.connection = connection

    def test_organization_system(self):
        chose_role_object = ChoseRole(self.driver)
        organization_identity_test_obj = OrganizationIdentityTest(self.driver, self.connection)
        chose_role_object.click_role_radio_btn()
        chose_role_object.click_continuation_btn()
        organization_identity_test_obj.test_add_organization_identity()