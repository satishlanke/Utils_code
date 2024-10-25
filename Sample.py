import java.util.Arrays;
import java.util.Scanner;

public class CoinChange {
    public static int coinChange(int[] coins, int amount) {
        // Initialize an array to store the minimum number of coins for each amount
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1); // Fill with a large number as an initial value
        dp[0] = 0; // Base case: 0 amount requires 0 coins

        // Iterate through all amounts from 1 to the target amount
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1); // Choose the coin and update the dp array
                }
            }
        }

        // If dp[amount] is still the large number, return -1 (not possible)
        return dp[amount] > amount ? -1 : dp[amount];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input the denominations of coins
        System.out.println("Enter the denominations of coins separated by spaces:");
        String[] coinInput = sc.nextLine().split(" ");
        int[] coins = new int[coinInput.length];
        for (int i = 0; i < coinInput.length; i++) {
            coins[i] = Integer.parseInt(coinInput[i]);
        }

        // Input the amount to be formed
        System.out.println("Enter the amount:");
        int amount = sc.nextInt();

        // Get the result and print it
        int result = coinChange(coins, amount);
        System.out.println("The fewest number of coins needed: " + result);
    }
}