def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    dependancy_count = {}
    dependents = {pack : [] for pack in packages}

    for package, dependencies in packages.items():
        valid_dep = [dep for dep in dependencies if dep in packages]
        dependancy_count[package] = len(valid_dep)

        for dep in valid_dep:
            dependents[dep].append(package)
    ready = sorted(dep for dep, count in dependancy_count.items() if count == 0)

    result = []

    while ready:
        package = ready.pop(0)
        result.append(package)

        for dependent in sorted(dependents[package]):
            dependancy_count[dependent] -= 1

            if dependancy_count[dependent] == 0:
                ready.append(dependent)
        ready.sort()

    if len(packages) != len(result):
        return []
    return result


print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # Expected: ["driver", "database", "app"]
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # Expected: ["A", "B", "C"]
print(package_dependency_resolver({}))  # Expected: []
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # Expected: []
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # Expected: ["api", "web", "backend", "frontend"]