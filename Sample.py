import java.util.Arrays;
import java.util.Scanner;

public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1); // Set all values to a large number
        dp[0] = 0; // Base case: 0 coins needed for amount 0

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (i - coin >= 0) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        // If we cannot make up the amount, return -1
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter coin denominations separated by spaces:");
        String[] coinStrings = scanner.nextLine().split(" ");
        int[] coins = new int[coinStrings.length];
        for (int i = 0; i < coinStrings.length; i++) {
            coins[i] = Integer.parseInt(coinStrings[i]);
        }
        
        System.out.println("Enter the amount:");
        int amount = scanner.nextInt();
        
        int result = coinChange(coins, amount);
        System.out.println("Minimum coins required: " + result);
    }
}