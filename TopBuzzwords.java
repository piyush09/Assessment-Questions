/* Problem is described in this link:
 * 
 * https://aonecode.com/amazon-online-assessment-top-n-buzzwords
 */




import java.util.List;
import java.util.ArrayList;
import java.util.*;

public class TopBuzzwords {

	
	private static ArrayList <String> topNCompetitors(int numCompetitors, int topNCompetitors, List<String> competitors, int numReviews, List<String> reviews)
	{
		
		
		int numToys = numCompetitors;
		int topToys = topNCompetitors;
		
		String[] toys = new String[competitors.size()];
		
		for(int i=0; i<toys.length; i++) {
			toys[i] = competitors.get(i);
			
		}
		
		int numQuotes = numReviews;
		String[] quotes = new String[reviews.size()]
;
		for (int i=0; i < quotes.length; i++) {
			quotes[i] = reviews.get(i);
		}
		
		Map<String, int[]> freq = new HashMap<>();
		
		for (String toy:toys) {
			freq.put(toy,  new int[] {0,0});
			
		}
		
		for (String quote: reviews) {
			
			Set <String> used = new HashSet<>();
			
			String[] words = quote.toLowerCase().split("\\W+");
			
			for (String word:words) {
				
				if (!freq.containsKey(word)) {
					continue;
				}
				
				int [] nums = freq.get(word);
				
				nums[0]++;
				
				if (!used.contains(word)) {
					nums[1]++;
				}
				
				used.add(word);
			}
		}
		
		
		PriorityQueue<String> pq = new PriorityQueue<>((t1, t2) -> {
			if (freq.get(t1)[0] != freq.get(t2)[0]) {
				return freq.get(t1)[0] - freq.get(t2)[0];
				
			}
			
			if (freq.get(t1)[1] != freq.get(t2)[1]) {
				return freq.get(t1)[1] - freq.get(t2)[1];
			}
			
			return t2.compareTo(t1);
		});
		
		if (topNCompetitors > numCompetitors) {
			
			for (String toy: freq.keySet()) {
				if (freq.get(toy)[0] > 0) {
					pq.add(toy);
				}
			}
			
		} else {
			
			for (String toy: competitors) {
				
				pq.add(toy);
				
				if (pq.size() > topNCompetitors) {
					pq.poll();
				}
			}
		}
	
		ArrayList<String> output = new ArrayList<>();
		
		while(!pq.isEmpty()) {
			output.add(pq.poll());
		}
		
		Collections.reverse(output);
		return output;
		
	}
	
	public static void main(String[] args) {
		int numToys = 6;
		int topToys = 2; 
		int numQuotes = 6; 
		List<String> toys = Arrays.asList("elmo", "elsa", "legos", "drone", "tablet", "warcraft");
		
		List<String>quotes = Arrays.asList(
				"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
				"The new Elmo dolls are super high quality",
				"Expect the Elsa dolls to be very popular this year, Elsa!",
				"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
				"For parents of older kids, look into buying them a drone",
				"Warcraft is slowly rising in popularity ahead of the holiday season"
				);
		

		System.out.println(topNCompetitors(numToys, topToys, toys, numQuotes, quotes));
	}
	
}
