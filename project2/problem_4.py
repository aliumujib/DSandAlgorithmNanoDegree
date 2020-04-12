class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
new_child = "new_child"
prodigal_child = "prodigal_child"

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_user(new_child)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name():
        return True

    if group:
        if user in group.users:
            return True
        else:
            if len(group.get_groups()) > 0:
                # return is_user_in_group(user, group.get_groups().pop()) I left this commented because I think it is
                # the same as having a loop, especially since the last item gets removed at each iteration,
                # I am not attached to the idea, but I am really trying to practise using recursion where I can and
                # this seemed like a good opportunity to do so. So I'd appreciate a quick explanation by my next
                # reviewer. :-)

                for grp in group.get_groups():
                    return is_user_in_group(user, grp)
            else:
                return False
    else:
        return False


print(is_user_in_group(new_child, parent))
print(is_user_in_group(None, parent))
print(is_user_in_group(prodigal_child, parent))
