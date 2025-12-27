public class Lasagna {

    // Tarefa 1: Retorna o tempo total esperado (40 min)
    public int expectedMinutesInOven() {
        return 40;
    }

    // Tarefa 2: Retorna quanto tempo falta (Esperado - Real)
    public int remainingMinutesInOven(int actualMinutes) {
        return expectedMinutesInOven() - actualMinutes;
    }

    // Tarefa 3: Cada camada leva 2 minutos
    public int preparationTimeInMinutes(int layers) {
        return layers * 2;
    }

    // Tarefa 4: Tempo total (Preparo das camadas + Tempo atual no forno)
    public int totalTimeInMinutes(int layers, int actualMinutes) {
        return preparationTimeInMinutes(layers) + actualMinutes;
    }
}