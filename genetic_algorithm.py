import 'package:flutter/material.dart';
import 'genetic_algorithm_page.dart'; // Import the Genetic Algorithm Page

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Aquarium Monitor',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Aquarium Monitor'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Placeholder for Live Video Feed
          Expanded(
            child: Container(
              color: Colors.blue[100],
              child: const Center(
                child: Text(
                  'Live Video Feed',
                  style: TextStyle(fontSize: 20, color: Colors.black54),
                ),
              ),
            ),
          ),
          // Control Buttons Section
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _buildActionButton(
                  context,
                  'Feed Now',
                  Colors.green,
                  () {
                    // Implement feed functionality here
                  },
                ),
                _buildActionButton(
                  context,
                  'Clean Now',
                  Colors.blue,
                  () {
                    // Implement clean functionality here
                  },
                ),
                _buildActionButton(
                  context,
                  'Genetic Algorithm',
                  Colors.orange,
                  () {
                    // Navigate to Genetic Algorithm Page
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => const GeneticAlgorithmPage()),
                    );
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // Function to build action buttons
  Widget _buildActionButton(BuildContext context, String label, Color color, VoidCallback onPressed) {
    return ElevatedButton(
      onPressed: onPressed,
      style: ElevatedButton.styleFrom(
        primary: color,
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
        textStyle: const TextStyle(fontSize: 16),
      ),
      child: Text(label),
    );
  }
}
