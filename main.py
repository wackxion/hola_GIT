"""
Script principal con menú para ejecutar las demos de `examples.py`.
Uso:
  python main.py           -> menú interactivo
  python main.py variables -> ejecuta la demo `variables`
"""

import sys
import examples


def print_menu():
    demos = examples.list_demos()
    print("Demos disponibles:")
    for i, d in enumerate(demos, 1):
        print(f"  {i}. {d}")
    print("  0. salir")
    return demos


def main():
    args = sys.argv[1:]
    if args:
        name = args[0]
        try:
            print(f"Ejecutando demo: {name}\n")
            examples.run_demo(name)
        except KeyError as e:
            print(e)
        return

    demos = print_menu()
    while True:
        try:
            choice = input("Seleccione demo (número o nombre): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSaliendo.")
            return
        if choice == "0":
            print("Saliendo.")
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(demos):
                name = demos[idx]
            else:
                print("Opción inválida")
                continue
        else:
            name = choice
        try:
            print("")
            examples.run_demo(name)
            print("")
        except KeyError:
            print("Demo no encontrada. Intente de nuevo.")


if __name__ == "__main__":
    main()
