import re
from urllib import request
import tomli
from project import Project


def package_name(dependency):
    # "flask>=3.1.3" -> "flask"
    return re.split(r"[<>=!~;\[ ]", dependency)[0]


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        data = tomli.loads(content)

        project = data["project"]
        dev = data.get("dependency-groups", {}).get("dev", [])

        return Project(
            project["name"],
            project.get("description", ""),
            project.get("license", ""),
            [author["name"] for author in project.get("authors", [])],
            [package_name(dep) for dep in project.get("dependencies", [])],
            [package_name(dep) for dep in dev],
        )