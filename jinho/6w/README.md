# ������
- ���� Ư���� �����ϴ� Ʈ�� ����� �ڷᱸ��.
- �ִ񰪰� �ּڰ��� ã�Ƴ��� ������ ������ �ϱ� ���� ������ ����������, ������ ���� �� ��ü�� `����`�� �Ǿ����� �ʴ�.

## Ư��
- �ּ���(Min Heap) : �θ� ��尡 �ڽĳ�� ������ �׻� ����
- �ִ���(Max Heap) : �θ� ��尡 �ڽĳ�� ������ �׻� ŭ

## ����(push)
<img src ="https://miro.medium.com/max/1920/1*jeELUYrAVbZJg6S1E2ujjA.gif">
������ ��� ������ ��� �ڿ� ������ �� �� min-heap ���� O(logN)

## ����(pop)

<img src="https://miro.medium.com/max/700/1*j6SmjQvS1-FPcONVtEkN1w.gif">
������ ��� ��Ʈ ���� ������ ��带 ������ �� ��Ʈ�������� min-heap ���� O(logN)


|�޼ҵ�|�ð����⵵
|-----|---------|
|heappush|O(logN)|
|heappop|O(logN)|
|heappushpop|O(logN)|
|heapify|O(NlogN)|


# heap����
 heap������ max-heap �������� pop�� n��ŭ �ݺ���Ų ��  �ð����⵵ : O(NlogN)
