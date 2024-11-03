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
          // Live Video Feed Placeholder
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
          // Control Buttons
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  onPressed: () {
                    // Implement feed functionality here
                  },
                  style: ElevatedButton.styleFrom(
                    primary: Colors.green,
                  ),
                  child: const Text('Feed Now'),
                ),
                ElevatedButton(
                  onPressed: () {
                    // Implement clean functionality here
                  },
                  style: ElevatedButton.styleFrom(
                    primary: Colors.blue,
                  ),
                  child: const Text('Clean Now'),
                ),
                ElevatedButton(
                  onPressed: () {
                    // Navigate to Genetic Algorithm Page
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => const GeneticAlgorithmPage()),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    primary: Colors.orange,
                  ),
                  child: const Text('Genetic Algorithm'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
