import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class Solution {
    public String[] solution(String[] players, String[] callings) {

        int numOfPlayers = players.length;
        Map<String, Integer> ranking = new HashMap<>();
        for (int i = 0; i < numOfPlayers; i++) {
            ranking.put(players[i], i);
        }

        for(String player : callings) {
            int rank = ranking.get(player);
            String frontPlayer = players[rank-1];
            ranking.replace(frontPlayer, rank);
            players[rank] = frontPlayer;

            ranking.replace(player, rank-1);
            players[rank-1] = player;
        }
        return players;
    }
}

