def rentang(data):
    return (min(data), max(data))


def ringkasan(data):
    return {
        "jumlah": len(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data),
    }


if __name__ == "__main__":
    data_uji = [12.0, 15.0, 15.0]
    r = ringkasan(data_uji)

    print(rentang(data_uji))
    print(r)
    print(r["rata"])