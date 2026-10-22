def package_dependency_resolver(
    packages: dict[str, list[str]]
) -> list[str]:
    dependencies_count = {}
    dependents = {package: [] for package in packages}

    # Count only dependencies that exist in the input.
    for package, dependencies in packages.items():
        valid_dependencies = [
            dep for dep in dependencies
            if dep in packages
        ]
        dependencies_count[package] = len(valid_dependencies)

        for dep in valid_dependencies:
            dependents[dep].append(package)

    # Start with packages that have no dependencies.
    ready = sorted(
        package
        for package, count in dependencies_count.items()
        if count == 0
    )

    result = []

    while ready:
        package = ready.pop(0)
        result.append(package)

        # Update packages that depend on the installed package.
        for dependent in sorted(dependents[package]):
            dependencies_count[dependent] -= 1

            if dependencies_count[dependent] == 0:
                ready.append(dependent)

        # Keep the next choice alphabetical.
        ready.sort()

    # If some packages remain, there is a cycle.
    if len(result) != len(packages):
        return []

    return result


print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))  # Expected: ["driver", "database", "app"]
print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))  # Expected: ["A", "B", "C"]
print(package_dependency_resolver({}))  # Expected: []
print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))  # Expected: []
print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))  # Expected: ["api", "web", "backend", "frontend"]