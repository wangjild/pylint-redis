# coding: utf-8

from __future__ import unicode_literals

import six
import astroid

from pylint.checkers import BaseChecker, utils
from pylint.interfaces import IAstroidChecker

BASE_ID = 86

class RedisChecker(BaseChecker):
    __implements__ = (IAstroidChecker,)
    name = 'pylint_redis'

    DANGER_FUNCTIONS = {
        'hgetall',
        'hkeys',
        'hvals',
        'smembers'
    }

    MESSAGE_ID = 'redis-bad-performance'
    msgs = {
        'E%d10' % BASE_ID: (
            "%s() is a bad performance command, check this usage again or ignore this error",
            MESSAGE_ID,
            "redis bad performance functions must be used carefully",
        ),
    }

    @utils.check_messages(MESSAGE_ID)
    def visit_call(self, node):
        """Called for every function call in the source code."""
        if not isinstance(node.func, astroid.Attribute):
            # It isn't a attribute call, can't deduce what function it is.
            return

        if node.func.attrname not in self.DANGER_FUNCTIONS:
            # Not a function we care about.
            return

        expr = node.func.expr

        if not isinstance(expr, (astroid.Name, astroid.Call)):
            return

        if not self.linter.is_message_enabled(self.MESSAGE_ID, line = node.fromlineno):
            return

        # Bad!
        self.add_message(self.MESSAGE_ID, args = node.func.attrname, node = node)

def register(linter):
    linter.register_checker(RedisChecker(linter))
