import sys

from all_plots import (
    plot_psp_vs_distance,
    plot_psp_vs_tau,
    plot_psp_vs_lambda,
    plot_ccp_vs_epsilon,
    plot_ccp_vs_lambda,
    plot_jpisac_vs_distance,
    plot_jpisac_vs_tau,
    plot_tradeoff,
    plot_beta
)


# MENU
def show_menu():
    print("\n========= 📊 PLOT MENU =========")
    print("1. PSP vs Distance")
    print("2. PSP vs Tau(sensing_threshold)")
    print("3. PSP vs Lambda_r")
    print("4. CCP vs Epsilon(communication_threshold)")
    print("5. CCP vs Lambda")
    print("6. JPISAC vs Distance")
    print("7. JPISAC vs Tau")
    print("8. PSP vs CCP (Tradeoff)")
    print("9. PSP & CCP vs Beta")
    print("10. Plot ALL graphs")
    print("0. Exit")
    print("================================\n")



# EXECUTION
def run_choice(choice):

    if choice == "1":
        plot_psp_vs_distance()
        
        
    elif choice == "2":
        plot_psp_vs_tau()
        
        
    elif choice == "3":
        plot_psp_vs_lambda()
        
        
    elif choice == "4":
        plot_ccp_vs_epsilon()
    
        
    elif choice == "5":
        plot_ccp_vs_lambda()
        
        
    elif choice == "6":
        plot_jpisac_vs_distance()
        
        
    elif choice == "7":
        plot_jpisac_vs_tau()
        
        
    elif choice == "8":
        plot_tradeoff()
        
        
    elif choice == "9":
        plot_beta()
        
        
    elif choice == "10":
        print("\n🚀 Plotting ALL graphs...\n")

        plot_psp_vs_distance()
        plot_psp_vs_tau()
        plot_psp_vs_lambda()

        plot_ccp_vs_epsilon()
        plot_ccp_vs_lambda()

        plot_jpisac_vs_distance()
        plot_jpisac_vs_tau()

        plot_tradeoff()
        plot_beta()

    elif choice == "0":
        print("Exiting...")
        sys.exit()

    else:
        print("❌ Invalid choice!")



# MAIN LOOP
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0–10): ").strip()
        run_choice(choice)


if __name__ == "__main__":
    main()