package CTF;

import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.Collection;

public class wayToProspecta implements aintNoGimletEye, noTraumaTeam{
	
	String babaroga;
	static ArrayList<String> vaultResponse = new ArrayList<String>();
	
	wayToProspecta(byte[] babaroga){
		this.babaroga=wayToProspecta.vaultPayload(babaroga);
	}
	
	wayToProspecta(String babaroga){
		this.babaroga=wayToProspecta.vaultPayload(babaroga);
	}

	public boolean checkBlackICE(String s) {
        return s.contains("flag") && s.length() > 5;
    }

    public String neuroShift(String t) {
        return t.substring(t.length() - 4) + t.substring(0, t.length() - 4);
    }

    public String ghostInject(String t) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t.length(); i++) {
            char c = t.charAt(i);
            if (i % 2 == 1)
                c = (char) (c ^ 0x39);
            sb.append(c);
        }
        return sb.toString();
    }

    public String datastreamMorph(String t) {
        int l = t.length() / 3;
        return t.substring(l, 2 * l) + t.substring(2 * l) + t.substring(0, l);
    }

    public String nanoModulate(String t) {
        int[] delta = {2, -2, 4, -4, 1, -1, 3, -3};
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t.length(); i++) {
            sb.append((char) (t.charAt(i) + delta[i % delta.length]));
        }
        return sb.toString();
    }

    public String cyberChain() {
    	String s = "";
        String[] stages = {"neuroShift", "ghostInject", "datastreamMorph", "nanoModulate"};
        for (String stage : stages) {
            switch (stage) {
                case "neuroShift":
                	s = neuroShift(this.babaroga);
                    break;
                case "ghostInject":
                	s = ghostInject(s);
                    break;
                case "datastreamMorph":
                	s = datastreamMorph(s);
                    break;
                case "nanoModulate":
                	s = nanoModulate(s);
                    break;
            }
        }
        return s;
    }

    public static String vaultPayload(String s) {
    	if (wayToProspecta.vaultResponse.isEmpty()) {
    		wayToProspecta.linearFrames();
    	}
    	return s;
    }
    public static String vaultPayload(byte[] babaroga) {
    	if (wayToProspecta.vaultResponse.isEmpty()) {
    		wayToProspecta.linearFrames();
    	}
    	String s;
    	try {
			s = new String (babaroga,"utf-8");
		} catch (UnsupportedEncodingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			s = "error";
		}
    	return s.trim();
    }
    
    public static void linearFrames() {
    	for(int i=0;i<12;i++) {
			wayToProspecta.vaultResponse.add("");
		}
		wayToProspecta.vaultResponse.set(3,"Signal intercepted... decryption in progress.");
		wayToProspecta.vaultResponse.set(1,"Intrusion detected. Trace initiated...");
		wayToProspecta.vaultResponse.set(6,"Signal intercepted... decryption in progress.");
		wayToProspecta.vaultResponse.set(4,"Access Denied: Length mismatch.");
		wayToProspecta.vaultResponse.set(8,"Signal intercepted... decryption in progress.");
		wayToProspecta.vaultResponse.set(0,"Enter access key to breach the Vault: ");
		wayToProspecta.vaultResponse.set(5,"Signal intercepted... decryption in progress.");
		wayToProspecta.vaultResponse.set(2,"Access Granted. You cracked it!");
		wayToProspecta.vaultResponse.set(7,"Signal intercepted... decryption in progress.");
    }

    public static void corpseRun(String str) {
        System.out.println(str);
    }
}
