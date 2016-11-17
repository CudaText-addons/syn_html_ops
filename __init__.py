from sw import *

def do_tag(tag):
    s = ed.get_text_sel()
    if not s: return msg_status('Text not selected')
    pos, nlen = ed.get_sel()
    ed.replace(pos, nlen, '<%s>%s</%s>' % (tag, s, tag))
    ed.set_sel(pos, nlen+3+4)
    msg_status('Added tag <%s>'%tag)


class Command:
    def do_b(self):
        do_tag('b')
    def do_i(self):
        do_tag('i')
    def do_u(self):
        do_tag('u')
