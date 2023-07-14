# DNS Benchmark Tool

This is a simple DNS benchmarking tool that performs DNS lookups to determine the average, minimum, maximum, and standard deviation times of DNS resolution for a specified hostname using specified DNS servers. 

## How It Works

This tool comprises two primary functions: `dns_lookup` and `benchmark_dns`. 

- `dns_lookup` performs a single DNS lookup for a specified hostname using a given DNS server, returning the elapsed time of the lookup. If the hostname cannot be resolved (due to a non-existent domain error), this function returns -1.

- `benchmark_dns` performs multiple DNS lookups as specified by `num_lookups`, collects the elapsed times of successful lookups, and computes statistical metrics: the average, minimum, maximum, and standard deviation of these times. If there are unsuccessful lookups, a message is printed. If all lookups are unsuccessful, an error message is printed.

## How to Use

In the script's main function, specify the hostname you want to perform DNS lookups on, the DNS server's IP address, and the number of lookups you want to perform.

Here is an example:

```python
if __name__ == "__main__":
    hostname = "www.ifms.edu.br"
    dns_server = "8.8.8.8"  # Replace with the desired DNS server IP
    num_lookups = 10
    print(f"Performing DNS benchmark for {hostname} with {num_lookups} queries using DNS server {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)

    hostname = "www.ifms.edu.br"
    dns_server = "8.8.4.4"  # Replace with the desired DNS server IP
    num_lookups = 10
    print(f"Performing DNS benchmark for {hostname} with {num_lookups} queries using DNS server {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)



vbnet
Copy code
# DNS Benchmark Tool

This is a simple DNS benchmarking tool that performs DNS lookups to determine the average, minimum, maximum, and standard deviation times of DNS resolution for a specified hostname using specified DNS servers. 

## How It Works

This tool comprises two primary functions: `dns_lookup` and `benchmark_dns`. 

- `dns_lookup` performs a single DNS lookup for a specified hostname using a given DNS server, returning the elapsed time of the lookup. If the hostname cannot be resolved (due to a non-existent domain error), this function returns -1.

- `benchmark_dns` performs multiple DNS lookups as specified by `num_lookups`, collects the elapsed times of successful lookups, and computes statistical metrics: the average, minimum, maximum, and standard deviation of these times. If there are unsuccessful lookups, a message is printed. If all lookups are unsuccessful, an error message is printed.

## How to Use

In the script's main function, specify the hostname you want to perform DNS lookups on, the DNS server's IP address, and the number of lookups you want to perform.

Here is an example:

```python
if __name__ == "__main__":
    hostname = "www.ifms.edu.br"
    dns_server = "8.8.8.8"  # Replace with the desired DNS server IP
    num_lookups = 10
    print(f"Performing DNS benchmark for {hostname} with {num_lookups} queries using DNS server {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)

    hostname = "www.ifms.edu.br"
    dns_server = "8.8.4.4"  # Replace with the desired DNS server IP
    num_lookups = 10
    print(f"Performing DNS benchmark for {hostname} with {num_lookups} queries using DNS server {dns_server}")
    benchmark_dns(hostname, dns_server, num_lookups)
In this example, we perform 10 DNS lookups on www.ifms.edu.br using two different DNS servers: 8.8.8.8 and 8.8.4.4. The results are printed to the console.

## Dependencies
This script uses the following Python libraries:

- time
- statistics
- dns.resolver (from the dnspython package)


If you do not have the dnspython package installed, you can install it using pip:
pip install dnspython

