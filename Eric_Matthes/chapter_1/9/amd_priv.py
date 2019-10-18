#9-11

#9-11 from imp_adm import Admin, Privileges, User

#9-12 User импортирован в imp_adm_priv, а imp_adm_priv сюда
from imp_adm_priv import Privileges, Admin

admi = Admin('john','galt',30,200,'passw-d')

admi.describe_user()
print('\n')
admi.privileges.show_privileges()