import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Random;

class SimuladorArduino {
    private final Random random;

    public SimuladorArduino() {
        this.random = new Random();
    }

    public float lerTemperatura() {
        return 0 + random.nextFloat() * 50;
    }

    public float lerUmidade() {
        return random.nextFloat() * 100;
    }

    public int lerLuminosidade() {
        return random.nextInt(1001);
    }

    public String lerHora() {
        LocalDateTime agora = LocalDateTime.now();
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm:ss");
        String horaFormatada = agora.format(formato);
        return horaFormatada;
    }

    public String analisarTemperatura(float temperatura) {
        if (temperatura > 27) {
            return "Altas temperaturas. Ligar ar condicionado ou sistema de ventilação.";
        } else if (temperatura < 18) {
            return "Baixas Temperaturas. Ligar o aquecedor.";
        } else {
            return "Temperatura agradável.";
        }
    }

    public String analisarUmidade(float umidade) {
        if (umidade > 65) {
            return "Alerta de Alta Umidade. Chances de chuva - fechar janelas e verificar vazamentos.";
        } else if (umidade < 30) {
            return "Alerta de Baixa Umidade. Ligar umidificador";
        } else {
            return "Umidade adequada";
        }
    }

    public String analisarLuminosidade(int luminosidade) {
        if (luminosidade > 800) {
            return "Ambiente Iluminado. Desligar luzes e abrir cortinas para economizar energia.";
        } else if (luminosidade < 120) {
            return "Ambiente escuro. Ligar as luzes.";
        } else {
            return "Iluminação adequada";
        }
    }

    public static void main(String[] args) {
        SimuladorArduino simulador = new SimuladorArduino();

        while (true) { 
            float temperatura = simulador.lerTemperatura();
            float umidade = simulador.lerUmidade();
            int luminosidade = simulador.lerLuminosidade();
            String horaAtual = simulador.lerHora();

            String msgTemperatura = simulador.analisarTemperatura(temperatura);
            String msgUmidade = simulador.analisarUmidade(umidade);
            String msgLuz = simulador.analisarLuminosidade(luminosidade);


            System.out.println("         >>-----" + horaAtual + " -----<<");
            System.out.printf("Temperatura: %.2f ºC | %s%n", temperatura, msgTemperatura);
            System.out.printf("Umidade: %.2f%%       | %s%n", umidade, msgUmidade);
            System.out.printf("Luminosidade: %d Lux | %s%n", luminosidade, msgLuz);
            System.out.println(">>----------------------------------------------------<<");            
            
            try {
                Thread.sleep(5000);
            } catch (InterruptedException e) {
                System.err.println("Erro de Leitura" + e.getMessage());
            }
        }
    }
}
