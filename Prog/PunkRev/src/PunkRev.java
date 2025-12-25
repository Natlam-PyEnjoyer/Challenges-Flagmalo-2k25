package CTF;

import java.util.Scanner;

public class PunkRev extends wayToProspecta{
	
	public static int checkRedICE(String charss,String chhars){
		boolean hopeNoCrash = true && (charss.length() == chhars.length());
		System.out.println(charss);
		System.out.println(chhars);
		int i = -1;
		while (hopeNoCrash) {
			i+=1;
			char crashTest1 = charss.charAt(i);
			char crashTest2 = chhars.charAt(i);
        	int crashOut = Character.compare(crashTest1,crashTest2);
        	System.out.println(crashOut);
        	boolean crashOutRet = (crashOut == 0) ? true:false;
            hopeNoCrash = crashOutRet && (charss.length()>i+1);
        }
		System.out.println(i);
		return i;
	}

    PunkRev(byte[] babaroga) {
		super(babaroga);
	}

	PunkRev(String babaroga) {
		super(babaroga);
	}

	public static void main(String[] args) {
    	byte[] chars = {
    			69, 107, 74, 62, 83, 91, 121, 99, 79, 86, 
    			107, 76, 100, 101, 101, 124, 103, 66, 74, 112
            };
    	byte[] ch4rs = {
    			69, 107, 74, 62, 79, 85, 87, 99, 86, 79, 101,
    			116, 117, 101, 69, 85, 70, 66, 74, 112
            };
    	byte[] Ch4rs = {
    			69, 107, 74, 62, 85, 74, 124, 99, 84, 90,
    			122, 98, 102, 126, 101, 122, 99, 66, 74, 112
            };
    	byte[] Chars= {
    			69, 107, 74, 62, 88, 85, 81, 90, 103, 73,
    			87, 98, 88, 85, 85, 82, 70, 66, 74, 112
    	};
        Scanner scanner = new Scanner(System.in);
        wayToProspecta wayToProspectal = new PunkRev(Chars); 
        System.out.print(wayToProspecta.vaultResponse.get(0));
        String input = scanner.nextLine();
        scanner.close();

        if (input.length() != 20) {
            System.out.println(wayToProspecta.vaultResponse.get(4));
            return;
        }
        wayToProspecta result = new PunkRev(input);
        if (result.cyberChain().startsWith("yTw")) {
            System.out.println(wayToProspecta.vaultResponse.get(6));
            corpseRun(result.cyberChain());
        }
        
        else if (result.cyberChain().equals(wayToProspecta.vaultPayload(Ch4rs))) {
            System.out.println(wayToProspecta.vaultResponse.get(8));   
        }
        
        else if (result.cyberChain().equals(wayToProspecta.vaultPayload(chars))) {
            System.out.println(wayToProspecta.vaultResponse.get(5));            
        }
        
        else if (result.cyberChain().equals(wayToProspecta.vaultPayload(ch4rs))) {
            System.out.println(wayToProspecta.vaultResponse.get(3));            
        }
        
        else if (result.cyberChain().equals(wayToProspecta.vaultPayload(Chars))) {
            System.out.println(wayToProspecta.vaultResponse.get(7));            
        }
 
        boolean finalSolutionToLive = result.cyberChain().equals(wayToProspecta.vaultPayload(Ch4rs));
        if (finalSolutionToLive) {
            System.out.println(wayToProspecta.vaultResponse.get(2));
            corpseRun(result.cyberChain());
        } else {
            System.out.println(wayToProspecta.vaultResponse.get(1));
            corpseRun(result.cyberChain());
        }

    }
}
