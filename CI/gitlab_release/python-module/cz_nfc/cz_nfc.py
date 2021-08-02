#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from commitizen import git
from commitizen.cz.base import BaseCommitizen


class nfc_cz(BaseCommitizen):
    bump_pattern = r"^(break|new|fix|hotfix|ci|docs)"
    bump_map = {"break": "MAJOR", "new": "MINOR", "fix": "PATCH", "hotfix": "PATCH", "ci": "PATCH", "docs": "PATCH"}

    changelog_pattern = "^(break|new|fix|hotfix|ci|docs)"
    change_type_order = ["BREAKING CHANGE", "feat", "fix", "refactor", "perf", "docs", "ci"]
    change_type_map = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "refactor": "Code Refactor",
        "perf": "Performance improvements",
        "docs": "Documentaton / Guides",
        "ci": "Continious Integration"
    }

    commit_parser = r"^(?P<change_type>feat|fix|refactor|perf|BREAKING CHANGE|ci|docs)(?:\((?P<scope>[^()\r\n]*)\)|\()?(?P<breaking>!)?:\s(?P<message>.*)?"


    def changelog_message_builder_hook(self, parsed_message: dict, commit: git.GitCommit) -> dict:
        rev = commit.rev
        m = parsed_message["message"]
        parsed_message["message"] = f"{rev} - {m}"
        return parsed_message


    def questions(self) -> list:
        raise NotImplementedError("Not Implemented yet")

    def message(self, answers: dict) -> str:
        raise NotImplementedError("Not Implemented yet")


discover_this = nfc_cz
