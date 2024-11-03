import 'package:flutter/material.dart';
import 'dart:math';

class GeneticAlgorithmPage extends StatefulWidget {
  const GeneticAlgorithmPage({super.key});

  @override
  _GeneticAlgorithmPageState createState() => _GeneticAlgorithmPageState();
}

class _GeneticAlgorithmPageState extends State<GeneticAlgorithmPage> {
  final int popSize = 500;
  final double mutRate = 0.2;
  final String target = 'fikri';
  final String genes = ' abcdefghijklmnopqrstuvwxyz';

  List<List<dynamic>> population = [];
  int generation = 1;
  bool found = false;

  void initializePop() {
    population.clear();
    for (int i = 0; i < popSize; i++) {
      List<String> chromosome = List.generate(target.length,
          (index) => genes[Random().nextInt(genes.length)]);
      population.add([chromosome, 0]);
    }
  }

  int fitnessCal(List<dynamic> chromoFromPop) {
    int difference = 0;
    for (int i = 0; i < target.length; i++) {
      if (target[i] != chromoFromPop[0][i]) {
        difference++;
      }
    }
    return difference;
  }

  List<List<dynamic>> selection() {
    population.sort((a, b) => a[1].compareTo(b[1]));
    return population.sublist(0, (0.5 * popSize).toInt());
  }

  List<List<dynamic>> crossover(List<List<dynamic>> selectedChromos) {
    List<List<dynamic>> offspring = [];
    for (int i = 0; i < popSize; i++) {
      var parent1 = selectedChromos[Random().nextInt(selectedChromos.length)][0];
      var parent2 = selectedChromos[Random().nextInt(selectedChromos.length)][0];
      int crossoverPoint = Random().nextInt(target.length);
      List<String> child = List.from(parent1.sublist(0, crossoverPoint)) +
          parent2.sublist(crossoverPoint);
      offspring.add([child, 0]);
    }
    return offspring;
  }

  List<List<dynamic>> mutate(List<List<dynamic>> offspring) {
    for (var arr in offspring) {
      for (int i = 0; i < arr[0].length; i++) {
        if (Random().nextDouble() < mutRate) {
          arr[0][i] = genes[Random().nextInt(genes.length)];
        }
      }
    }
    return offspring;
  }

  void replace(List<List<dynamic>> newGen) {
    for (int i = 0; i < population.length; i++) {
      if (population[i][1] > newGen[i][1]) {
        population[i][0] = newGen[i][0];
        population[i][1] = newGen[i][1];
      }
    }
  }

  void runGeneticAlgorithm() {
    initializePop();
    while (!found) {
      for (var chromo in population) {
        chromo[1] = fitnessCal(chromo);
      }

      if (population[0][1] == 0) {
        setState(() {
          found = true;
        });
        break;
      }

      var selected = selection();
      var offspring = crossover(selected);
      var mutated = mutate(offspring);
      replace(mutated);

      setState(() {
        generation++;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Genetic Algorithm'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            if (found)
              Text(
                'Target found: ${population[0][0].join()} in Generation: $generation',
                style: const TextStyle(fontSize: 18),
              )
            else
              ElevatedButton(
                onPressed: runGeneticAlgorithm,
                child: const Text('Start Genetic Algorithm'),
              ),
          ],
        ),
      ),
    );
  }
}
