import time
import statistics
import dns.resolver

def dns_lookup(hostname, dns_server):
    start_time = time.time()
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]

    try:
        resolver.resolve(hostname, 'A')
        elapsed_time = time.time() - start_time
    except dns.resolver.NXDOMAIN:
        elapsed_time = -1

    return elapsed_time

def benchmark_dns(hostname, dns_server, num_lookups=100):
    lookup_times = []

    for _ in range(num_lookups):
        elapsed_time = dns_lookup(hostname, dns_server)
        if elapsed_time >= 0:
            lookup_times.append(elapsed_time)
        else:
            print(f"Erro ao resolver {hostname}")

    if len(lookup_times) > 0:
        avg_time = statistics.mean(lookup_times)
        min_time = min(lookup_times)
        max_time = max(lookup_times)
        stddev_time = statistics.stdev(lookup_times) if len(lookup_times) > 1 else 0

        print(f"Média: {avg_time:.4f} segundos")
        print(f"Mínimo: {min_time:.4f} segundos")
        print(f"Máximo: {max_time:.4f} segundos")
        print(f"Desvio padrão: {stddev_time:.4f} segundos")
    else:
        print(f"Não foi possível resolver {hostname} em nenhuma tentativa")

if __name__ == "__main__":
    hostname = "www.ifms.edu.br"
    dns_server = "8.8.8.8"  # Substitua pelo IP do servidor DNS desejado
    num_lookups = 10
    print(f"Fazendo benchmark de DNS para {hostname} com {num_lookups} consultas usando o servidor DNS {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)

    hostname = "www.ifms.edu.br"
    dns_server = "8.8.4.4"  # Substitua pelo IP do servidor DNS desejado
    num_lookups = 10
    print(f"Fazendo benchmark de DNS para {hostname} com {num_lookups} consultas usando o servidor DNS {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)
