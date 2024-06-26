import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;

public class SoloRider {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int m = scanner.nextInt();

        // Store passengers and vehicles
        Map<String, Passenger> passengers = new HashMap<>();
        Map<String, Vehicle> vehicles = new HashMap<>();

        // Read passenger information
        for (int i = 0; i < n; i++) {
            String name = scanner.next();
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            passengers.put(name, new Passenger(name, x, y));
        }

        // Read vehicle information
        for (int i = 0; i < m; i++) {
            String id = scanner.next();
            int x = scanner.nextInt();
            int y = scanner.nextInt();

            vehicles.put(id, new Vehicle(id, x, y));
        }

        // Prioritize passengers based on name
        PriorityQueue<Passenger> pq = new PriorityQueue<>(Comparator.comparing(Passenger::getName));
        pq.addAll(passengers.values());

        // Track assigned vehicles
        Map<Passenger, Vehicle> assignments = new HashMap<>();

        // Assign vehicles to passengers
        while (!pq.isEmpty()) {
            Passenger passenger = pq.poll();

            Vehicle nearestVehicle = null;
            int minDistance = Integer.MAX_VALUE;

            // Find nearest idle vehicle
            for (Vehicle vehicle : vehicles.values()) {
                if (assignments.containsKey(vehicle)) {
                    continue;
                }

                int distance = manhattanDistance(passenger.x, passenger.y, vehicle.x, vehicle.y);

                if (distance == minDistance) {
                    if (nearestVehicle == null || nearestVehicle.id.compareTo(vehicle.id) > 0) {
                        nearestVehicle = vehicle;
                    }
                } else if (distance < minDistance) {
                    minDistance = distance;
                    nearestVehicle = vehicle;
                }
            }

            // Assign the vehicle and update the state
            assignments.put(passenger, nearestVehicle);
            vehicles.remove(nearestVehicle.id);
        }

        // Calculate total distance traveled
        int totalDistance = 0;
        for (Map.Entry<Passenger, Vehicle> entry : assignments.entrySet()) {
            Passenger passenger = entry.getKey();
            Vehicle vehicle = entry.getValue();

            totalDistance += manhattanDistance(passenger.x, passenger.y, vehicle.x, vehicle.y);
        }

        System.out.print(totalDistance);
    }

    private static int manhattanDistance(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2);
    }

    static class Passenger {
        String name;
        int x;
        int y;

        public Passenger(String name, int x, int y) {
            this.name = name;
            this.x = x;
            this.y = y;
        }

        public String getName() {
            return name;
        }
    }

    static class Vehicle {
        String id;
        int x;
        int y;

        public Vehicle(String id, int x, int y) {
            this.id = id;
            this.x = x;
            this.y = y;
        }
    }
}