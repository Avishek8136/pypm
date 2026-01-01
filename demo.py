"""
Demo Script - Interactive PyPM Demonstration
Shows the complete workflow with visual output
"""

from pathlib import Path
import tempfile

from pypm import CentralPackageStore, EnvironmentManager, PackageLoader


def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70)


def print_section(text):
    """Print a section header"""
    print(f"\n>>> {text}")


def create_demo_package(name: str, version: str, temp_dir: Path) -> Path:
    """Create a simple demo package"""
    pkg_dir = temp_dir / f"{name}-{version}"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    
    init_file = pkg_dir / "__init__.py"
    init_file.write_text(f'__version__ = "{version}"\n\ndef hello():\n    return "Hello from {name} v{version}!"')
    
    return pkg_dir


def main():
    print_header("PyPM - Python Package Manager Demo")
    print("\nThis demo shows how PyPM eliminates package duplication")
    print("while maintaining multiple environments with different versions.")
    
    input("\nPress Enter to start the demo...")
    
    # Initialize
    print_section("Step 1: Initialize PyPM Components")
    store = CentralPackageStore()
    env_manager = EnvironmentManager()
    loader = PackageLoader(store, env_manager)
    print("✓ Central Store initialized")
    print("✓ Environment Manager initialized")
    print("✓ Package Loader initialized")
    
    input("\nPress Enter to continue...")
    
    # Create demo packages
    print_section("Step 2: Create Demo Packages")
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        
        print("Creating 5 package versions:")
        packages = [
            ("calculator", "1.0.0"),
            ("calculator", "2.0.0"),
            ("formatter", "1.5.0"),
            ("validator", "3.2.1"),
            ("utils", "0.9.0"),
        ]
        
        pkg_paths = {}
        for name, version in packages:
            pkg_path = create_demo_package(name, version, temp_path)
            pkg_paths[f"{name}@{version}"] = pkg_path
            print(f"  ✓ {name} v{version}")
        
        input("\nPress Enter to continue...")
        
        # Add to central store
        print_section("Step 3: Add Packages to Central Store")
        print("Adding packages (each version stored ONLY ONCE):")
        for name, version in packages:
            store.add_package(name, version, str(pkg_paths[f"{name}@{version}"]))
        
        input("\nPress Enter to continue...")
        
        # Show store info
        print_section("Step 4: Central Store Statistics")
        info = store.get_store_info()
        print(f"  Store Location: {info['store_path']}")
        print(f"  Total Package Versions: {info['total_versions']}")
        print(f"  Unique Packages: {info['unique_packages']}")
        print(f"  Storage Used: {info['total_size_mb']} MB")
        
        print("\n  All packages in store:")
        for pkg in store.list_packages():
            print(f"    • {pkg['name']} v{pkg['version']}")
        
        input("\nPress Enter to continue...")
        
        # Create environments
        print_section("Step 5: Create Multiple Environments")
        environments = [
            ("web_app", "Web application environment"),
            ("api_service", "REST API service"),
            ("data_pipeline", "Data processing pipeline"),
        ]
        
        for env_name, desc in environments:
            env_manager.create_environment(env_name, desc)
            print(f"  ✓ Created '{env_name}'")
        
        input("\nPress Enter to continue...")
        
        # Configure environments
        print_section("Step 6: Configure Environments with Different Versions")
        
        print("\n  web_app environment:")
        env_manager.add_package_to_env("web_app", "calculator", "2.0.0")
        env_manager.add_package_to_env("web_app", "formatter", "1.5.0")
        env_manager.add_package_to_env("web_app", "validator", "3.2.1")
        print("    - calculator v2.0.0")
        print("    - formatter v1.5.0")
        print("    - validator v3.2.1")
        
        print("\n  api_service environment:")
        env_manager.add_package_to_env("api_service", "calculator", "1.0.0")  # Different version!
        env_manager.add_package_to_env("api_service", "validator", "3.2.1")
        env_manager.add_package_to_env("api_service", "utils", "0.9.0")
        print("    - calculator v1.0.0  [different version!]")
        print("    - validator v3.2.1")
        print("    - utils v0.9.0")
        
        print("\n  data_pipeline environment:")
        env_manager.add_package_to_env("data_pipeline", "formatter", "1.5.0")
        env_manager.add_package_to_env("data_pipeline", "utils", "0.9.0")
        print("    - formatter v1.5.0")
        print("    - utils v0.9.0")
        
        input("\nPress Enter to continue...")
        
        # Verify environments
        print_section("Step 7: Verify All Environments")
        for env_name, _ in environments:
            result = loader.verify_environment(env_name)
            status_symbol = "✓" if result['status'] == 'complete' else "✗"
            print(f"  {status_symbol} {env_name}: {result['total_packages']} packages - {result['status'].upper()}")
        
        input("\nPress Enter to continue...")
        
        # Show efficiency
        print_section("Step 8: Storage Efficiency Analysis")
        print("\n  Traditional Approach (with duplication):")
        print("    web_app:      calculator, formatter, validator  = 3 packages")
        print("    api_service:  calculator, validator, utils      = 3 packages")
        print("    data_pipeline: formatter, utils                 = 2 packages")
        print("    " + "-" * 60)
        print("    TOTAL: 8 package copies stored on disk")
        
        print("\n  PyPM Approach (centralized, no duplication):")
        print("    Central Store:")
        print("      - calculator v1.0.0")
        print("      - calculator v2.0.0")
        print("      - formatter v1.5.0")
        print("      - validator v3.2.1")
        print("      - utils v0.9.0")
        print("    " + "-" * 60)
        print("    TOTAL: 5 unique package versions + 3 tiny JSON files")
        
        print("\n  💾 Storage Savings: 37.5% reduction!")
        print("     (8 copies → 5 unique versions)")
        
        input("\nPress Enter to continue...")
        
        # Key benefits
        print_section("Step 9: Key Benefits Summary")
        print("\n  ✅ No Duplication:")
        print("     Each package version stored only once")
        
        print("\n  ✅ Version Flexibility:")
        print("     Different environments can use different versions")
        print("     (web_app uses calculator 2.0, api_service uses 1.0)")
        
        print("\n  ✅ Efficient Management:")
        print("     Lightweight JSON manifests for each environment")
        
        print("\n  ✅ Easy Activation:")
        print("     Load only the packages you need per environment")
        
        print("\n  ✅ Storage Savings:")
        print("     Scales with number of environments (more envs = more savings)")
        
        input("\nPress Enter to continue...")
        
        # Show environment list
        print_section("Step 10: Final Environment Overview")
        envs = env_manager.list_environments()
        print(f"\n  Total Environments: {len(envs)}")
        print(f"\n  {'Environment':<20} {'Packages':<10} {'Description':<30}")
        print("  " + "-" * 60)
        for env in envs:
            print(f"  {env['name']:<20} {env['package_count']:<10} {env['description']:<30}")
        
        print_header("Demo Complete!")
        print("\nWhat we demonstrated:")
        print("  1. Created 5 package versions in central store")
        print("  2. Created 3 different environments")
        print("  3. Configured each with specific package versions")
        print("  4. Achieved 37.5% storage reduction")
        print("  5. Maintained version flexibility")
        
        print("\nNext steps:")
        print("  - Try: python pypm.py list")
        print("  - Try: python pypm.py list-envs")
        print("  - Try: python pypm.py show-env web_app")
        print("  - Try: python pypm.py verify web_app")
        
        print("\nThank you for trying PyPM! 🚀")


if __name__ == '__main__':
    main()
