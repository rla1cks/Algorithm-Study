import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		
		String a = st2.nextToken();
		
		char temp = a.charAt(0);
		
		//연속된 알파벳 갯수 리스트
		ArrayList<Integer> cnlist = new ArrayList<>();
		
		int cc = 1;
		
		for (int i=1; i<N; i++) {
			if (temp == a.charAt(i)) {
				cc++;	//연속된 알파벳 수
				continue;
			}
			cnlist.add(cc);
			cc =1;
			temp = a.charAt(i);
		}
			cnlist.add(cc);

		//리스트 길이
		int ll = cnlist.size();
		if (ll<3) {
			System.out.println(0);
			System.exit(0);
		}else if(ll==3) {
			System.out.println(Math.min(Math.min(cnlist.get(0),cnlist.get(1)),cnlist.get(2)));
			System.exit(0);
		}
		
		//짝수번
		int even=0;
		int lasti = 0;
		for (int i=0; i<ll; i=i+2) {
			even = even + cnlist.get(i);
			lasti= cnlist.get(i);
		}
		if (cnlist.size()%2==1) {
			even = even - Math.max(cnlist.get(0),lasti);
		}else {
			even = even -cnlist.get(0);
		}
		//홀수번
		int odd=0;
		for (int i=1; i<ll; i=i+2) {
			odd = odd + cnlist.get(i);
			lasti = cnlist.get(i);
		}
		if (cnlist.size()%2==0) {
			odd = odd -lasti;
		}
		
		System.out.println(Math.min(even, odd));
		
	}
}
