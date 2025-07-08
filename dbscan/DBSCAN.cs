using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class DBSCAN : MonoBehaviour
{
    public GameObject spherePrefab;

    public float epsilon = 2f;
    public int minPoints = 3;
    public int numSpheres = 100;
    
    private List<Sphere> spheres = new List<Sphere>();
    
    // Start is called before the first frame update

    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private class Sphere
    {
        public GameObject sphereObject;
        public Vector3 position;
        public bool visited;
        public int clusterId;

        public sphere(GameObject sphereObject, Vector3 position)
        {
            this.sphereObject = sphereObject;
        }

    }


