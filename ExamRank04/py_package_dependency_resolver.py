def package_dependency_resolver(
    packages: dict[str, list[str]]
) -> list[str]:
    dependencies_count = {}
    dependents = {package: [] for package in packages}

    for pack, depenedies in packages.items():
        valid = [dep for dep in depenedies if dep in packages]
        dependencies_count[pack] = len(valid)

        for dep in valid:
            dependents[dep].append(pack)

    ready = sorted(dep for dep, count in dependencies_count.items() if count == 0)

    result = []
    
    while ready:
        result.extend(ready)
        next_ready = []

        for dep in ready:
            for dependent in dependents[dep]:
                dependencies_count[dependent] -=1 

                if dependencies_count[dependent] == 0:
                    next_ready.append(dependent)

        ready = sorted(next_ready)    
    if len(result) != len(packages):
            return []
    
    return result


print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # Expected: ["driver", "database", "app"]
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # Expected: ["A", "B", "C"]
print(package_dependency_resolver({}))  # Expected: []
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # Expected: []
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # Expected: ["api", "web", "backend", "frontend"]
