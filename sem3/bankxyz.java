import java.util.Scanner;

class Bank{

	private String Name = "safu master";
	private int Acc_No = 2192;
	private float Balance = 10000000;
	Scanner read = new Scanner(System.in);

	public void Deposite(){
		long amt;
		System.out.print("Enter Deposite Amount: ");
		amt = read.nextInt();
		Balance = Balance + amt;
		System.out.println("Account Balance: " + Balance);
	}
	
	public void Withdraw(){
		long amt;
		System.out.print("Enter Withdrawal Amount: ");
		amt = read.nextInt();
		if(amt<=Balance){
			Balance = Balance - amt;
			System.out.println("Account Balance: " + Balance);
		} else {
			System.out.println("Insuficirnt Amount!!");
		}
	}
	
	public void Details(){
		System.out.println("Account Holder: "+Name);
		System.out.println("Account Number: "+Acc_No);
		System.out.println("Account Balance: "+Balance);
	}
}

class Enum{
	public static void main(String []args){
		Scanner read = new Scanner(System.in);
		Bank PNB = new Bank();
		
		int opt;
		System.out.println("Select Any one Option");
		System.out.println("(1) ==> Account Details.");
		System.out.println("(2) ==> Deposite to Account.");
		System.out.println("(3) ==> Withdrawal from Account.");
		opt = read.nextInt();
		
		switch(opt){
			case 1:
				PNB.Details();
				break;
			case 2:
				PNB.Deposite();
				break;
			case 3:
				PNB.Withdraw();
				break;
			default:
				System.out.println("Please Select From The Above Options!!");
				break;
		}
	}
}
